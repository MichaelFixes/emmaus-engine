from pydantic import BaseModel, Field, model_validator


class BibleReference(BaseModel):
    book: str = Field(min_length=1)
    chapter: int = Field(ge=1)
    verse_start: int = Field(ge=1)
    verse_end: int | None = Field(default=None, ge=1)

    @model_validator(mode="after")
    def validate_range(self) -> "BibleReference":
        if self.verse_end is not None and self.verse_end < self.verse_start:
            raise ValueError(
                "verse_end doit être supérieur ou égal à verse_start"
            )
        return self

    def display(self) -> str:
        if self.verse_end is None:
            verse_part = str(self.verse_start)
        else:
            verse_part = f"{self.verse_start}-{self.verse_end}"

        return f"{self.book} {self.chapter}:{verse_part}"
