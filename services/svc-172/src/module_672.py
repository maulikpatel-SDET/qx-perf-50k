"""Service module 672: business logic, no crypto."""


def calculate_total_672(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_672():
    return 'module 672 handles orders and invoices'
