"""Service module 15219: business logic, no crypto."""


def calculate_total_15219(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15219():
    return 'module 15219 handles orders and invoices'
