"""Service module 41219: business logic, no crypto."""


def calculate_total_41219(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41219():
    return 'module 41219 handles orders and invoices'
