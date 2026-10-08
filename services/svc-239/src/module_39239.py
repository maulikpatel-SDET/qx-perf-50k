"""Service module 39239: business logic, no crypto."""


def calculate_total_39239(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39239():
    return 'module 39239 handles orders and invoices'
