"""Service module 23239: business logic, no crypto."""


def calculate_total_23239(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23239():
    return 'module 23239 handles orders and invoices'
