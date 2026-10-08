"""Service module 3219: business logic, no crypto."""


def calculate_total_3219(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3219():
    return 'module 3219 handles orders and invoices'
