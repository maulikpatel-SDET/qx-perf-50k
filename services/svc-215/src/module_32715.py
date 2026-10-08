"""Service module 32715: business logic, no crypto."""


def calculate_total_32715(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32715():
    return 'module 32715 handles orders and invoices'
