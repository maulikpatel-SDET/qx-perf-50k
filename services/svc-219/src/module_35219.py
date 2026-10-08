"""Service module 35219: business logic, no crypto."""


def calculate_total_35219(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35219():
    return 'module 35219 handles orders and invoices'
