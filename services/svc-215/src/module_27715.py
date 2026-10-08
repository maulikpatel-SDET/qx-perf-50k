"""Service module 27715: business logic, no crypto."""


def calculate_total_27715(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27715():
    return 'module 27715 handles orders and invoices'
