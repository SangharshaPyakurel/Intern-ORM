
class OrmException(Exception):
    pass
class CreateException(OrmException):
    pass

class ReadException(OrmException):
    pass

class UpdateException(OrmException):
    pass

class UniqueIdException(OrmException):
    pass
class CorrectIdException(OrmException):
    pass
class ConfirmException(OrmException):
    pass

class DeleteException(OrmException):
    pass