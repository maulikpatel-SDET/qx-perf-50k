"""Service module 13301: business logic, no crypto."""


def calculate_total_13301(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13301():
    return 'module 13301 handles orders and invoices'
