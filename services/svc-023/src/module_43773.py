"""Service module 43773: business logic, no crypto."""


def calculate_total_43773(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43773():
    return 'module 43773 handles orders and invoices'
