from __future__ import annotations

from abc import ABC
from typing import Any, TypedDict


class AppContext(TypedDict):
    formal_name: str
    app_name: str
    class_name: str
    module_name: str
    project_name: str
    description: str
    author: str
    author_email: str
    bundle: str
    url: str
    license: str
    briefcase_version: str
    template_source: str
    template_branch: str


class BaseGuiBootstrap(ABC):
    """Definition for a plugin that defines a new Briefcase app."""

    fields: list[str] = [
        "app_source",
        "app_start_source",
        "pyproject_table_briefcase_extra_content",
        "pyproject_table_briefcase_app_extra_content",
        "pyproject_requires",
        "pyproject_test_requires",
        "pyproject_table_macOS",
        "pyproject_table_linux",
        "pyproject_table_linux_system_debian",
        "pyproject_table_linux_system_rhel",
        "pyproject_table_linux_system_suse",
        "pyproject_table_linux_system_arch",
        "pyproject_table_linux_appimage",
        "pyproject_table_linux_flatpak",
        "pyproject_table_windows",
        "pyproject_table_iOS",
        "pyproject_table_android",
        "pyproject_table_web",
        "pyproject_extra_content",
    ]

    def __init__(self, context: AppContext):
        # context contains metadata about the app being created
        self.context = context

    def extra_context(self) -> dict[str, Any] | None:
        """Runs prior to other plugin hooks to provide additional context.

        This can be used to prompt the user with additional questions or run arbitrary
        logic to supplement the context provided to cookiecutter.
        """

    def app_source(self) -> str | None:
        """The Python source code for app.py."""

    def app_start_source(self) -> str | None:
        """The Python source code for __main__.py to start the app."""

    def pyproject_table_briefcase_extra_content(self) -> str | None:
        """Additional content for ``tool.briefcase`` table."""

    def pyproject_table_briefcase_app_extra_content(self) -> str | None:
        """Additional content for ``tool.briefcase.app.<app-name>`` table."""

    def pyproject_requires(self) -> str | None:
        """List of package requirements for all platforms and formats."""

    def pyproject_test_requires(self) -> str | None:
        """List of package requirements for running tests."""

    def pyproject_table_macOS(self) -> str | None:
        """Content for ``tool.briefcase.app.<app-name>.macOS`` table."""

    def pyproject_table_linux(self) -> str | None:
        """Content for ``tool.briefcase.app.<app-name>.linux`` table."""

    def pyproject_table_linux_system_debian(self) -> str | None:
        """Content for ``tool.briefcase.app.<app-name>.linux.debian`` table."""

    def pyproject_table_linux_system_rhel(self) -> str | None:
        """Content for ``tool.briefcase.app.<app-name>.linux.rhel`` table."""

    def pyproject_table_linux_system_suse(self) -> str | None:
        """Content for ``tool.briefcase.app.<app-name>.linux.suse`` table."""

    def pyproject_table_linux_system_arch(self) -> str | None:
        """Content for ``tool.briefcase.app.<app-name>.linux.arch`` table."""

    def pyproject_table_linux_appimage(self) -> str | None:
        """Content for ``tool.briefcase.app.<app-name>.linux.appimage`` table."""

    def pyproject_table_linux_flatpak(self) -> str | None:
        """Content for ``tool.briefcase.app.<app-name>.linux.flatpak`` table."""

    def pyproject_table_windows(self) -> str | None:
        """Content for ``tool.briefcase.app.<app-name>.windows`` table."""

    def pyproject_table_iOS(self) -> str | None:
        """Content for ``tool.briefcase.app.<app-name>.iOS`` table."""

    def pyproject_table_android(self) -> str | None:
        """Content for ``tool.briefcase.app.<app-name>.android`` table."""

    def pyproject_table_web(self) -> str | None:
        """Content for ``tool.briefcase.app.<app-name>.web`` table."""

    def pyproject_extra_content(self) -> str | None:
        """Additional TOML to add to the bottom of pyproject.toml."""
