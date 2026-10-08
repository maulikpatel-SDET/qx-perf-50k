"""Service module 38219: business logic, no crypto."""


def calculate_total_38219(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38219():
    return 'module 38219 handles orders and invoices'
