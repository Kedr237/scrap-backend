'''
Custom field types.

Types:
- str_50
'''

from typing_extensions import Annotated

str_50 = Annotated[str, 50]
