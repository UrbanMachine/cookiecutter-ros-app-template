from shutil import which

from .errors import CommandError
from .paths import JS_PATH
from .run_command import run_command


def lint_eslint(fix: bool) -> None:
    if which("npx") is None:
        raise CommandError("Could not find the 'npx' command. Is Node.js installed?")

    additional_args = ["--fix"] if fix else []
    run_command(["npx", "eslint", *additional_args, "."], cwd=JS_PATH)
