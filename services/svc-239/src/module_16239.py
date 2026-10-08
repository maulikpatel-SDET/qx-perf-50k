"""Service module 16239: business logic, no crypto."""


def calculate_total_16239(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16239():
    return 'module 16239 handles orders and invoices'
