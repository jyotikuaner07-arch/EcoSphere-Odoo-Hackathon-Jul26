"""
core/exceptions.py

Custom exception classes for business-rule violations across EcoSphere.

Why this file exists:
- Services should raise a meaningful, named exception (e.g. InsufficientPointsError)
  instead of a generic Exception or raising an HTTPException directly.
- This keeps business logic (services/) completely decoupled from HTTP concerns -
  a service doesn't need to know what status code or JSON shape an error becomes.
- A single global handler (middleware/error_handler.py, built in a later step) will
  catch AppException and convert it into a consistent JSON response:
      { "error_code": "...", "message": "..." }
  using each exception's `status_code` and `error_code`.

Every exception below carries:
- error_code: a stable string the frontend can switch on (never change this
  once the frontend starts relying on it - treat it like an API contract).
- message: a human-readable explanation, safe to show directly in a UI.
- status_code: the HTTP status this should map to.
"""


class AppException(Exception):
    """
    Base class for all custom application exceptions.
    Never raise this directly - always raise a specific subclass below.
    """

    error_code: str = "APP_ERROR"
    status_code: int = 400

    def __init__(self, message: str = "An application error occurred."):
        self.message = message
        super().__init__(message)


class NotFoundError(AppException):
    """
    Raised when a requested resource (department, challenge, reward, etc.)
    doesn't exist. Pass the resource name and id for a clear message.
    """

    error_code = "NOT_FOUND"
    status_code = 404

    def __init__(self, resource: str, resource_id):
        message = f"{resource} with id '{resource_id}' was not found."
        super().__init__(message)


class InsufficientPointsError(AppException):
    """Raised during reward redemption when the employee's balance is too low."""

    error_code = "INSUFFICIENT_POINTS"
    status_code = 400

    def __init__(self, message: str = "You do not have enough points to redeem this reward."):
        super().__init__(message)


class OutOfStockError(AppException):
    """Raised during reward redemption when the reward's stock is zero."""

    error_code = "OUT_OF_STOCK"
    status_code = 400

    def __init__(self, message: str = "This reward is currently out of stock."):
        super().__init__(message)


class EvidenceRequiredError(AppException):
    """
    Raised when trying to approve a CSR/Challenge participation without a
    proof_url attached, while the evidence requirement setting is enabled.
    """

    error_code = "EVIDENCE_REQUIRED"
    status_code = 400

    def __init__(self, message: str = "Proof/evidence is required before this can be approved."):
        super().__init__(message)


class NoEmissionFactorConfiguredError(AppException):
    """Raised when a Carbon Transaction references an Emission Factor that doesn't exist."""

    error_code = "NO_EMISSION_FACTOR_CONFIGURED"
    status_code = 400

    def __init__(self, message: str = "No matching Emission Factor is configured for this transaction."):
        super().__init__(message)


class InvalidCredentialsError(AppException):
    """Raised on login when email/password don't match."""

    error_code = "INVALID_CREDENTIALS"
    status_code = 401

    def __init__(self, message: str = "Invalid email or password."):
        super().__init__(message)


class BadRequestError(AppException):
    """Raised when a request has invalid parameters or violates a business rule."""

    error_code = "BAD_REQUEST"
    status_code = 400

    def __init__(self, message: str = "Invalid request."):
        super().__init__(message)


class PermissionDeniedError(AppException):
    """Raised when a logged-in user's role doesn't allow the requested action."""

    error_code = "PERMISSION_DENIED"
    status_code = 403

    def __init__(self, message: str = "You do not have permission to perform this action."):
        super().__init__(message)