"""Service module 28235: business logic, no crypto."""


def calculate_total_28235(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28235():
    return 'module 28235 handles orders and invoices'
