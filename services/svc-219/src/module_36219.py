"""Service module 36219: business logic, no crypto."""


def calculate_total_36219(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36219():
    return 'module 36219 handles orders and invoices'
