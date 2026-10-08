"""Service module 38301: business logic, no crypto."""


def calculate_total_38301(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38301():
    return 'module 38301 handles orders and invoices'
