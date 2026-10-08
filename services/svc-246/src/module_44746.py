"""Service module 44746: business logic, no crypto."""


def calculate_total_44746(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44746():
    return 'module 44746 handles orders and invoices'
