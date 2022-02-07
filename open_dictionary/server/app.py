import pathlib

import fastapi
import pkg_resources
import sqlalchemy.exc

from open_dictionary.server.errors import ApiException
from open_dictionary.server.handlers import handle_api_error, handle_sqlalchemy_not_found, handle_sqlalchemy_multiple_results, handle_generic_error
from open_dictionary.server.routes.api.users.v1.router import router as router_api_user_v1

with open(pathlib.Path(__file__).parent.joinpath("description.md")) as file:
    description = file.read()

app = fastapi.FastAPI(
    debug=__debug__,
    title="Open Dictionary",
    description=description,
    version=pkg_resources.get_distribution("open_dictionary").version,
)

app.include_router(router_api_user_v1)


app.add_exception_handler(ApiException, handle_api_error)
app.add_exception_handler(sqlalchemy.exc.NoResultFound, handle_sqlalchemy_not_found)
app.add_exception_handler(sqlalchemy.exc.MultipleResultsFound, handle_sqlalchemy_multiple_results)
app.add_exception_handler(Exception, handle_generic_error)