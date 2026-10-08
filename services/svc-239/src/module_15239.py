"""Service module 15239: business logic, no crypto."""


def calculate_total_15239(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15239():
    return 'module 15239 handles orders and invoices'
