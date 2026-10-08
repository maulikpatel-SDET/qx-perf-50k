"""Service module 239: business logic, no crypto."""


def calculate_total_239(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_239():
    return 'module 239 handles orders and invoices'
