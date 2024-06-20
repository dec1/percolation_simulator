import os


class Config:
    # set env var "CI" to disable default plot generation

    @classmethod
    def want_plots(Cls):
        """Allow toggling off default plots generation eg in CI environment."""
        is_ci = os.getenv('CI') == 'true'
        return not is_ci
