"""Service module 44219: business logic, no crypto."""


def calculate_total_44219(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44219():
    return 'module 44219 handles orders and invoices'
