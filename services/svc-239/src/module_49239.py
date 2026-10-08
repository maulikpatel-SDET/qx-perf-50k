"""Service module 49239: business logic, no crypto."""


def calculate_total_49239(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49239():
    return 'module 49239 handles orders and invoices'
