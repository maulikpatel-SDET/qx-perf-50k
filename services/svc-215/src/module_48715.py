"""Service module 48715: business logic, no crypto."""


def calculate_total_48715(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48715():
    return 'module 48715 handles orders and invoices'
