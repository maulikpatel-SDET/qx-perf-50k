"""Service module 28239: business logic, no crypto."""


def calculate_total_28239(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28239():
    return 'module 28239 handles orders and invoices'
