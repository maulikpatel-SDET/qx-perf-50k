"""Service module 37239: business logic, no crypto."""


def calculate_total_37239(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37239():
    return 'module 37239 handles orders and invoices'
