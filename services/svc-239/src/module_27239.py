"""Service module 27239: business logic, no crypto."""


def calculate_total_27239(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27239():
    return 'module 27239 handles orders and invoices'
