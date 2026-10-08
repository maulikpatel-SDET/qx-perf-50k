"""Service module 36102: business logic, no crypto."""


def calculate_total_36102(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36102():
    return 'module 36102 handles orders and invoices'
