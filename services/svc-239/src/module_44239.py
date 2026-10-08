"""Service module 44239: business logic, no crypto."""


def calculate_total_44239(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44239():
    return 'module 44239 handles orders and invoices'
