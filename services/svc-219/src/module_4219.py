"""Service module 4219: business logic, no crypto."""


def calculate_total_4219(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4219():
    return 'module 4219 handles orders and invoices'
