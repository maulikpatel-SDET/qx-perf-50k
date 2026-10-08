"""Service module 46235: business logic, no crypto."""


def calculate_total_46235(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46235():
    return 'module 46235 handles orders and invoices'
