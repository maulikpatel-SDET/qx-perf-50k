"""Service module 27273: business logic, no crypto."""


def calculate_total_27273(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27273():
    return 'module 27273 handles orders and invoices'
