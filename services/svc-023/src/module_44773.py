"""Service module 44773: business logic, no crypto."""


def calculate_total_44773(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44773():
    return 'module 44773 handles orders and invoices'
