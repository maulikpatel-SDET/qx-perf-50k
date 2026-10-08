"""Service module 6219: business logic, no crypto."""


def calculate_total_6219(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6219():
    return 'module 6219 handles orders and invoices'
