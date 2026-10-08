"""Service module 21219: business logic, no crypto."""


def calculate_total_21219(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21219():
    return 'module 21219 handles orders and invoices'
