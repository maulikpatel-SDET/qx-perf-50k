"""Service module 34219: business logic, no crypto."""


def calculate_total_34219(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34219():
    return 'module 34219 handles orders and invoices'
