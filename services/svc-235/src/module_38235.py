"""Service module 38235: business logic, no crypto."""


def calculate_total_38235(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38235():
    return 'module 38235 handles orders and invoices'
