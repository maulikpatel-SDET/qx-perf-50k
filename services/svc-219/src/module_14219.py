"""Service module 14219: business logic, no crypto."""


def calculate_total_14219(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14219():
    return 'module 14219 handles orders and invoices'
