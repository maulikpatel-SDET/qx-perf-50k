"""Service module 48219: business logic, no crypto."""


def calculate_total_48219(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48219():
    return 'module 48219 handles orders and invoices'
