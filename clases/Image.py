#! /usr/bin/env python3
from attr import dataclass, field

PIXEL_SPLIT = 16

@dataclass
class Image:
    type: str = field(default="P2")
    path: str = field(default="")
    comment: str = field(default="")
    rows: int = field(default=0)
    columns: int = field(default=0)
    vector: list[int] = field(default=[])

    def __copy__(self):
        return Image(type=self.type, path=self.path, comment=self.comment, rows=self.rows, columns=self.columns,
            vector=self.vector.copy())

    def __dict__(self):
        return {
            "type": self.type,
            "path": self.path,
            "comment": self.comment,
            "rows": self.rows,
            "columns": self.columns
        }

    def __str__(self):
        return str(self.__dict__())

    def set_pixel(self, row, column, value):
        self.vector[(row * self.columns) + column] = value

    def set_pixel_pos(self, lugar, value):
        self.vector[lugar] = value

    def get_pixel(self, row, column):
        """
        return pixel
        """
        return self.vector[(row * self.columns) + column]

    def get_pixel_pos(self, lugar):
        """
        return pixel2
        """
        return self.vector[lugar]

    def save_pgm(self, file_path: str) -> None:
        with open(file_path, "w") as f1:
            f1.write(
                self.type
                + "\n"
                + self.comment
                + "\n"
                + str(self.rows)
                + " "
                + str(self.columns)
                + "\n255\n"
            )
            for ff in range(0, (self.rows * self.columns)):
                f1.write(str(self.get_pixel_pos(ff)) + "\n")

    def save(self) -> None:
        print(self.path)
        self.save_pgm(self.path)

    def show(self) -> None:
        print(
            self.type
            + "\n"
            + self.comment
            + "\n"
            + str(self.rows)
            + " "
            + str(self.columns)
            + "\n255\n"
        )
        for f1 in range(0, self.rows):
            for c1 in range(0, self.columns):
                print(str(self.get_pixel(f1, c1)))


if __name__ == "__main__":
    print("Clase Image")
