"""Service module 7219: business logic, no crypto."""


def calculate_total_7219(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7219():
    return 'module 7219 handles orders and invoices'
