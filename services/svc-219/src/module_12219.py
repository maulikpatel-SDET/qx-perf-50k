"""Service module 12219: business logic, no crypto."""


def calculate_total_12219(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12219():
    return 'module 12219 handles orders and invoices'
