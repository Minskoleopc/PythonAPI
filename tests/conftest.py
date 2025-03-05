# import pytest 
# def pytest_sessionstart(session):
#     print('Intialization for test session')

# def pytest_sessionfinish(session,exitstatus):
#     print(f'Test finsih with the session and status {exitstatus}')

# # Log test setup
# def pytest_runtest_setup(item):
#     print(f'Preparing test:{item.name}')

# # Log test teardown
# def pytest_runtest_teardown(item):
#     print(f'Cleaning up the data after test')

# #Order of test
# def pytest_collection_modifyitems(items):
#     items.sort(key=lambda x :"smoke" not in x.keyswords)
