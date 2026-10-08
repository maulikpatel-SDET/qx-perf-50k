"""Service module 11949: business logic, no crypto."""


def calculate_total_11949(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11949():
    return 'module 11949 handles orders and invoices'
