"""Service module 4349: business logic, no crypto."""


def calculate_total_4349(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4349():
    return 'module 4349 handles orders and invoices'
