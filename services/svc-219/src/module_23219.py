"""Service module 23219: business logic, no crypto."""


def calculate_total_23219(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23219():
    return 'module 23219 handles orders and invoices'
