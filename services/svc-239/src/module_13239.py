"""Service module 13239: business logic, no crypto."""


def calculate_total_13239(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13239():
    return 'module 13239 handles orders and invoices'
